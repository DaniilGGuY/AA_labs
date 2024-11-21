#ifndef CONVEYER_H__
#define CONVEYER_H__

#define URLS   "..\\urls.txt"

#include <queue>
#include <thread>
#include <mutex>
#include <ctime>

#include "conveyer_task.h"
#include "logger.h"

static std::mutex mtx1, mtx2, mtx3;

class Conveyer {
public:
	Conveyer(int col_files);
	
	void execute();

	void generate();

	void first_process();

	void second_process();

	void third_process();

private:
	std::queue<std::shared_ptr<ConveyerTask>> _first_queue;
	std::queue<std::shared_ptr<ConveyerTask>> _second_queue;
	std::queue<std::shared_ptr<ConveyerTask>> _third_queue;
	std::thread _threads[4];
	std::vector<std::shared_ptr<ConveyerTask>> _pool_tasks;
	std::vector<std::string> _urls;
	std::shared_ptr<Logger> _logger;
	int _col_files;
};

#endif