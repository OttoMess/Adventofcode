#include <fstream>
#include <vector>


void removeLastN(std::string &str, int n) {    // no-const
    if (str.length() < n) {
        return ;
    }
 
    str.erase(str.length() - n);
}

void SetPath(){
	std::string pathname;

    pathname = std::filesystem::current_path().string();
    removeLastN(pathname, 4);

    std::filesystem::current_path(pathname);
    std::cout << "Path set to: " << pathname << std::endl;
}

std::vector<std::string> TXTtoVector(std::string str){
	// making vector for storing the data
	std::vector<std::string> data;
	std::string line;
	std::ifstream myfile (str, std::ios::in);

	while(std::getline (myfile,line))
		data.push_back(line);
	return data;
}


