#ifndef RECIEPT_H__
#define RECIEPT_H__

#define ISSUE_ID    9159

#include <string>
#include <vector>

class Reciept {
public:
	Reciept(int id, std::string url, std::string title, std::string autor, 
			std::vector<std::string> ingr, std::vector<std::string> steps);

	std::string to_json();

private:
	int _id;
	int _issue_id = ISSUE_ID;
	std::string _url;
	std::string _title;
	std::string _author;
	std::vector<std::string> _ingredients;
	std::vector<std::string> _steps;
};

#endif