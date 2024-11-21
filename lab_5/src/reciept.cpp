#include "reciept.h"

Reciept::Reciept(int id, 
				 std::string url, 
				 std::string title, 
				 std::string author,
			     std::vector<std::string> ingr, 
				 std::vector<std::string> steps) 
	: _id(id), _url(url), _title(title), _author(author), _ingredients(ingr), _steps(steps) {}


std::string Reciept::to_json() {
	std::string json_imp;

	json_imp.append("[{");

	json_imp.append("\"id\":\"" + std::to_string(_id) + "\",");

	json_imp.append("\"issue_id\":\"" + std::to_string(_issue_id) + "\",");

	json_imp.append("\"url\":\"" + _url + "\",");

	json_imp.append("\"title\":\"" + _title + "\",");

	json_imp.append("\"author\":\"" + _author + "\",");

	json_imp.append("\"ingredients\":[");
	for (int i = 0; i < _ingredients.size(); ++i)
		json_imp.append("{\"name\":\"" + _ingredients[i] + "\"},");
	json_imp[json_imp.size() - 1] = ']';
	json_imp.append(",");

	json_imp.append("\"steps\":[");
	for (int i = 0; i < _steps.size(); ++i)
		json_imp.append("{\"name\":\"" + _steps[i] + "\"},");
	json_imp[json_imp.size() - 1] = ']';

	json_imp.append("}]");

	return json_imp;
}

