#include "logger.h"

clock_t Logger::log(int task_id, std::string comment)
{
	mt_log.lock();
	clock_t now = clock();
	std::cout << "TASK: " << task_id << "; TIME: " << now << "; COMM: " << comment << std::endl;
	mt_log.unlock();

	return now;
}
