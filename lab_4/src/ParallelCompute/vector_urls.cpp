#include "vector_urls.h"

void read_urls_from_file(std::vector<std::string>& urls, std::string filename, int max_col)
{
	std::ifstream in(filename);

	for (int i = 0; i < max_col; ++i)
	{
		std::string url;
		getline(in, url);
		urls.push_back(url);
	}

	in.close();
}