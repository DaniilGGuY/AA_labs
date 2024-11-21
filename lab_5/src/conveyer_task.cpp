#include "conveyer_task.h"
#include <iostream>

ConveyerTask::ConveyerTask(std::string filename, std::string url, int id) 
    : _filename_input(filename), _url(url), _task_id(id) { };

std::string ConveyerTask::read_data() {
    std::string line;

    std::ifstream in(READ_DIR + _filename_input);
    if (in.is_open())
        while (std::getline(in, line))
            _data += line;
    in.close();

    return _data;
}

std::shared_ptr<Reciept> ConveyerTask::filter_data() {
    // +- начало блока с рецептом в html файле
    // 4 = len("<h1 ")
    _filter_data = _data.substr(_data.find("itemprop=\"name\"") - 4, _data.size());
    // +- конец блока с рецептом в html файле
    // 2 = len("</")
    _filter_data.erase(_filter_data.find("article") - 2, _filter_data.size());
    // Необходимые для парсинга параметры
    std::string title, author;
    std::vector<std::string> ingredients, steps;
    // Цикл обработки данных
    int start, finish;
    while ((start = _filter_data.find("<")) != -1 && (finish = _filter_data.find(">")) != -1) {
        if (finish < start) {
            _filter_data.erase(finish, 1);
            continue;
        }
        std::string tag = _filter_data.substr(start, finish - start + 1);
        int pos;
        if ((pos = tag.find("itemprop=\"name\"")) != -1) {
            title = _filter_data.substr(finish + 1, _filter_data.size());
            int endpos = title.find("<");
            if (endpos != -1)
                title.erase(endpos, title.size());
        }
        else if ((pos = tag.find("itemprop=\"author\"")) != -1) {
            author = _filter_data.substr(finish + 1, _filter_data.size());
            int endpos = author.find("<");
            if (endpos != -1)
                author.erase(endpos, author.size());
        }
        else if ((pos = tag.find("itemprop=\"ingredients\"")) != -1) {
            std::string ingr = _filter_data.substr(finish + 1, _filter_data.size());
            int endpos = ingr.find("<");
            if (endpos != -1)
                ingr.erase(endpos, ingr.size());
            ingredients.push_back(ingr);
        }
        else if ((pos = tag.find("class=\"instruction\"")) != -1) {
            if (_filter_data[finish + 1] == '<') {
                _filter_data.erase(start, finish - start + 1);
                start = _filter_data.find("<");
                finish = _filter_data.find(">");
            }

            std::string step = _filter_data.substr(finish + 1, _filter_data.size());
            int endpos = step.find("<");
            if (endpos != -1)
                step.erase(endpos, step.size());
            steps.push_back(step);
        }

        _filter_data.erase(start, finish - start + 1);
    }
    
    _reciept = std::make_shared<Reciept>(Reciept(_task_id, _url, title, author, ingredients, steps));

	return _reciept;
}

void ConveyerTask::write_data() {
    std::string filename = "data" + std::to_string(_task_id) + ".json";
    std::ofstream out(WRITE_DIR + filename);
    out << _reciept->to_json();
    out.close();
}

void ConveyerTask::set_crt(clock_t create_time) { _create_time = create_time;  }

void ConveyerTask::set_fqt(clock_t first_queue_time) { _first_queue_time = first_queue_time; }

void ConveyerTask::set_sqt(clock_t second_queue_time) { _second_queue_time = second_queue_time; }

void ConveyerTask::set_tqt(clock_t third_queue_time) { _third_queue_time = third_queue_time; }

void ConveyerTask::set_fpt(clock_t first_processor_time) { _first_processor_time = first_processor_time; }

void ConveyerTask::set_spt(clock_t second_processor_time) { _second_processor_time = second_processor_time;  }

void ConveyerTask::set_tpt(clock_t third_processor_time) { _third_processor_time = third_processor_time;  }

void ConveyerTask::set_drt(clock_t destroy_time) { _destroy_time = destroy_time;  }

clock_t ConveyerTask::get_existance_time() { return _destroy_time - _create_time; }

clock_t ConveyerTask::get_first_wait() { return _first_processor_time - _first_queue_time; }

clock_t ConveyerTask::get_second_wait() { return _second_processor_time - _second_queue_time; }

clock_t ConveyerTask::get_third_wait() { return _third_processor_time - _third_queue_time; }

clock_t ConveyerTask::get_first_proc() { return _second_queue_time - _first_processor_time; }

clock_t ConveyerTask::get_second_proc() { return _third_queue_time - _second_processor_time; }

clock_t ConveyerTask::get_third_proc() { return _destroy_time - _third_processor_time; }
