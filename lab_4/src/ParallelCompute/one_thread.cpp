#include "one_thread.h"

double calc_one_thread_work(std::vector<std::string> urls, std::string dirname, int col_exps)
{
	clock_t begin = clock();
	for (int exp = 0; exp < col_exps; ++exp)
	{
		for (int i = 0; i < urls.size(); ++i)
		{
			std::string filename = dirname + "data" + std::to_string(i) + ".txt";
			url_to_string(urls[i], filename);
		}
	}
	clock_t end = clock();

	return double(end - begin) / CLOCKS_PER_SEC / col_exps;
}
