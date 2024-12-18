#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>
#include <chrono>
#include <vector>
#include <filesystem>

#include "c_lib.h"

using namespace std;

int part1(string str)
{
	stringstream ss;
	
	ss << str;
	string temp;
	int number, game_id, i, cubes;
	i = 0;
	while (!ss.eof()){
		ss >> temp;

		if (stringstream(temp) >> number) {
  			
			if (i == 0){ // getting the first int. this is the game number
				game_id = number;
			}
			else{ // if not the first int, it is a count of cubes
				cubes = number;
			}
			i++;
		} 
		// finding the color of the cubes (int) found above
		else{
			if (cubes <=12){  // quickly continue if no dice count is above 12
				continue;
			}

			else if (temp.find("blue") != string::npos){
				if (cubes > 14){
					return 0;
				}
			} 

			else if (temp.find("red") != string::npos){
				if (cubes > 12){
					return 0;
				}
			}

			else if (temp.find("green") != string::npos){
				if (cubes > 13){
					return 0;
				}
			}
		}
	}
	// cout << "\n";
	return game_id;
}

int part2(string str){
	stringstream ss;
	
	ss << str;
	string temp;
	int number, game_id, i, cubes, blues=0, reds=0, greens=0, total=0;
	i = 0;
	while (!ss.eof()){
		ss >> temp;

		if (stringstream(temp) >> number) {
  			
			if (i == 0){ // getting the first int. this is the game number
				game_id = number;
			}
			else{ // if not the first int, it is a count of cubes
				cubes = number;
			}
			i++;
		} 
		// finding the color of the cubes (int) found above
		else{
			if (temp.find("blue") != string::npos && cubes > blues){
				blues = cubes;
			} 

			else if (temp.find("red") != string::npos && cubes > reds){
				reds = cubes;
			} 

			else if (temp.find("green") != string::npos && cubes > greens){
				greens = cubes;
			} 
		}
		
	}
	total = reds * greens * blues;
	return total;
}

void RunBothParts(vector<string> data){
		int game_id=0, output=0, part2_output = 0;

		for (auto i : data){
			output += part1(i);
			part2_output += part2(i);
	}
	
	cout << "part1 output: " << output << "\n";
	cout << "part2 output: " << part2_output << "\n";
}


int main() {
	auto t1 = chrono::high_resolution_clock::now();
	cout << "    ### Running program ###\n";
  	// declaring variables:
    filesystem::current_path("C:\\C-storage\\GitHub\\Adventofcode\\2023");
		
	int game_id=0, output=0, part2_output = 0;
	string s, line;
	vector<string> data_example, data;

	data_example = TXTtoVector("data/day2_example.txt");
	data = TXTtoVector("data/day2.txt");

	cout << "\n" << "example file" << "\n";
	RunBothParts(data_example);
	cout << "\n" << "full data" << "\n";
	RunBothParts(data);
	
	cout << "    ### Program ended ###" << "\n";

	auto t2 = chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<chrono::microseconds>( t2 - t1 ).count();
	cout <<"\n" <<  duration<< " microseconds";
  	return 0;
}