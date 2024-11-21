#include "conveyer.h"

Conveyer::Conveyer(int col_files) : _col_files(col_files) {
	std::fstream urls(URLS);

	for (int i = 0; i < col_files; ++i) {
		std::string str;
		getline(urls, str);
		_urls.push_back(str);
	}

	urls.close();

	_logger = std::make_shared<Logger>(Logger());
}

void Conveyer::execute()
{
	_threads[0] = std::thread(&Conveyer::generate, this);
	_threads[1] = std::thread(&Conveyer::first_process, this);
	_threads[2] = std::thread(&Conveyer::second_process, this);
	_threads[3] = std::thread(&Conveyer::third_process, this);

	for (int i = 0; i < 4; ++i)
		_threads[i].join();

	double ex_avg = 0, fq_avg = 0, sq_avg = 0, tq_avg = 0, fp_avg = 0, sp_avg = 0, tp_avg = 0;
	int len = _pool_tasks.size();
	for (int i = 0; i < len; ++i) {
		ex_avg += _pool_tasks[i]->get_existance_time();
		fq_avg += _pool_tasks[i]->get_first_wait();
		sq_avg += _pool_tasks[i]->get_second_wait();
		tq_avg += _pool_tasks[i]->get_third_wait();
		fp_avg += _pool_tasks[i]->get_first_proc();
		sp_avg += _pool_tasks[i]->get_second_proc();
		tp_avg += _pool_tasks[i]->get_third_proc();
	}
	ex_avg /= len, fq_avg /= len, sq_avg /= len, tq_avg /= len, fp_avg /= len, sp_avg /= len, tp_avg /= len;

	std::cout << std::endl << "RESULT OF SIMULATION" << std::endl;
	std::cout << "Average existance time: " << ex_avg << std::endl;
	std::cout << "Average first queue wait time: " << fq_avg << std::endl;
	std::cout << "Average second queue wait time: " << sq_avg << std::endl;
	std::cout << "Average third queue wait time: " << tq_avg << std::endl;
	std::cout << "Average first process time: " << fp_avg << std::endl;
	std::cout << "Average second process time: " << sp_avg << std::endl;
	std::cout << "Average third process time: " << tp_avg << std::endl;
}

void Conveyer::generate() {
	for (int i = 0; i < _col_files; ++i) {
		std::shared_ptr<ConveyerTask> task = std::make_shared<ConveyerTask>(
			ConveyerTask("data" + std::to_string(i) + ".txt", _urls[i], i));
		task->set_crt(_logger->log(i + 1, "task created"));
		mtx1.lock();
		_first_queue.push(task);
		task->set_fqt(_logger->log(i + 1, "in first queue"));
		mtx1.unlock();
	}
}

void Conveyer::first_process() {
	int id_task = 0;
	while (id_task != _col_files) {
		mtx1.lock();
		if (_first_queue.empty()) {
			mtx1.unlock();
			continue;
		}
		std::shared_ptr<ConveyerTask> active_task = _first_queue.front();
		_first_queue.pop();
		mtx1.unlock();
		active_task->set_fpt(_logger->log(id_task + 1, "at first station"));
		active_task->read_data();
		mtx2.lock();
		_second_queue.push(active_task);
		active_task->set_sqt(_logger->log(id_task + 1, "in second queue"));
		mtx2.unlock();
		++id_task;
	}
}

void Conveyer::second_process() {
	int id_task = 0;
	while (id_task != _col_files) {
		mtx2.lock();
		if (_second_queue.empty()) {
			mtx2.unlock();
			continue;
		}
		std::shared_ptr<ConveyerTask> active_task = _second_queue.front();
		_second_queue.pop();
		mtx2.unlock();
		active_task->set_spt(_logger->log(id_task + 1, "at second station"));
		active_task->filter_data();
		mtx3.lock();
		_third_queue.push(active_task);
		active_task->set_tqt(_logger->log(id_task + 1, "in third queue"));
		mtx3.unlock();
		++id_task;
	}
}

void Conveyer::third_process() {
	int id_task = 0;
	while (id_task != _col_files) {
		mtx3.lock();
		if (_third_queue.empty()) {
			mtx3.unlock();
			continue;
		}
		std::shared_ptr<ConveyerTask> active_task = _third_queue.front();
		_third_queue.pop();
		mtx3.unlock();
		active_task->set_tpt(_logger->log(id_task + 1, "at third station"));
		active_task->write_data();
		_pool_tasks.push_back(active_task);
		active_task->set_drt(_logger->log(id_task + 1, "processed"));
		++id_task;
	}
}
