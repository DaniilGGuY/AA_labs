#ifndef CONVEYER_TASK_H__
#define CONVEYER_TASK_H__

#define READ_DIR         "..\\data\\"
#define WRITE_DIR   "..\\data_json\\"

#include <fstream>
#include <string>
#include <ctime>

#include "reciept.h"

class ConveyerTask
{
public:
	ConveyerTask(std::string filename, std::string url, int id);

	std::string read_data();

	std::shared_ptr<Reciept> filter_data();

	void write_data();

	void set_crt(clock_t create_time);
	void set_fqt(clock_t first_queue_time);
	void set_sqt(clock_t second_queue_time);
	void set_tqt(clock_t third_queue_time);
	void set_fpt(clock_t first_processor_time);
	void set_spt(clock_t second_processor_time);
	void set_tpt(clock_t third_processor_time);
	void set_drt(clock_t destroy_time);

	clock_t get_existance_time();
	clock_t get_first_wait();
	clock_t get_second_wait();
	clock_t get_third_wait();
	clock_t get_first_proc();
	clock_t get_second_proc();
	clock_t get_third_proc();

private:
	std::shared_ptr<Reciept> _reciept;
	std::string _filename_input;
	std::string _data;
	std::string _url;
	std::string _filter_data;
	int _task_id;

	clock_t _create_time;
	clock_t _first_queue_time;
	clock_t _second_queue_time;
	clock_t _third_queue_time;
	clock_t _first_processor_time;
	clock_t _second_processor_time;
	clock_t _third_processor_time;
	clock_t _destroy_time;
};

#endif