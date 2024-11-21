#ifndef LOGGER_H__
#define LOGGER_H__

#include <ctime>
#include <string>
#include <iostream>
#include <mutex>

static std::mutex mt_log;

class Logger
{
public:
	Logger() = default;
	static clock_t log(int task_id, std::string comment);
};

#endif