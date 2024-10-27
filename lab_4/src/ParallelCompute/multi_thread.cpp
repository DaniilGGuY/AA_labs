#include "multi_thread.h"

void thread_func(std::vector<std::string> *urls, std::string dirname, int index)
{
	my_mtx.lock();
	std::string filename = dirname + "data" + std::to_string(index) + ".txt";
	std::string url = (*urls)[index];
	my_mtx.unlock();

	url_to_string(url, filename);
}

double calc_multi_threads_work(std::vector<std::string> urls, std::string dirname, int col_threads, int col_exps)
{
	std::thread threads[100];

	clock_t begin = clock();
	for (int exp = 0; exp < col_exps; ++exp)
	{
		int index = 0;
		while (index < urls.size())
		{
			int col_worked_threads = 0;
			for (int i = 0; i < col_threads && index < urls.size(); i++, index++, col_worked_threads++)
				threads[i] = std::thread(thread_func, &urls, dirname, index);

			for (int i = 0; i < col_worked_threads; i++)
				threads[i].join();
		}
	}
	clock_t end = clock();

	return double(end - begin) / CLOCKS_PER_SEC / col_exps;
}