#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>
#include <chrono>

using namespace std;

int part1(string str)
{
	// cout << str << endl;
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
				// cout << "game number: "<< game_id << endl;
			}
			else{ // if not the first int, it is a count of cubes
				cubes = number;
			}
			i++;
		} 
		// finding the color of the cubes (int) found above
		else{
			if (cubes <=12){
				continue;
			}

			else if (temp.find("blue") != string::npos){
				// cout << cubes <<" blue cubes" << endl;
				if (cubes > 14){
					return 0;
				}
			} 

			else if (temp.find("red") != string::npos){
				// cout << cubes <<" red cubes" << endl;
				if (cubes > 12){
					return 0;
				}
			}

			else if (temp.find("green") != string::npos){
				// cout << cubes <<" green cubes" << endl;
				if (cubes > 13){
					return 0;
				}
			}
		}
	}
	// cout << endl;
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


// int NumberOfLines(string str){
// 	//  find the number of lines in the text file
// 	int lines=0;
// 	ifstream myfile (str, ios::in);
// 	string unused;
// 	while (getline(myfile, unused))
// 		lines++;
	
// 	return lines;
// }


// array<string,5> TXTtoDataArray(string str, int lines) {
// 	// building an array with all the lines of the text file
// 	// string data[lines], line;
// 	array<string,5> data;
// 	int i=0;

// 	ifstream file (str, ios::in);
// 	while (getline (file, line)){
// 		data[i] = line;
// 		i++;
// 	}
// 	return data;
// }





int main() {
	auto t1 = chrono::high_resolution_clock::now();
	cout << "    ### Running program ###\n";
  	// declaring variables:
	int game_id=0, output=0, part2_output = 0;
	string s, line, data;


	// data = TXTtoDataArray("data/day2_example.txt", NumberOfLines("data/day2_example.txt"));
	// test = NumberOfLine("data/day2.txt");
	
	// string data[lines];

  	// ifstream myfile ("data/day2_example.txt", ios::in);
	ifstream myfile ("data/day2.txt", ios::in);
 	
	if (myfile.is_open())
  	{
    	while ( getline (myfile,line) ){
			output += part1(line);
			part2_output += part2(line);
    	}

    	myfile.close();
		cout << "part1 output: " << output << "\n";
		cout << "part2 output: " << part2_output << "\n";
		cout << "    ### Program ended ###" << "\n";
  	}


  	// else cout << "Unable to open file";
	auto t2 = chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<chrono::microseconds>( t2 - t1 ).count();
	cout << duration<< " microseconds";
  	return 0;
}
