#include <vector>
#include <fstream>
#include <iostream>
#include <filesystem>
#include <sstream>
#include <bits/stdc++.h>
#include <ranges>


#include "c_lib.h"

using namespace std;

vector<int> FindIntString(string str){
    stringstream ss;
	vector<int> numbers;
	ss << str;
	string temp;
	int number;
	
    while (!ss.eof()){
		ss >> temp;

		if (stringstream(temp) >> number) {
            numbers.push_back(number);
		} 
    }
    sort(numbers.begin(), numbers.end());
    return numbers;
}

int FindPoints(string str){
    int start_base, start_check, score=0; 
    string play_string, check_string;
    vector<int> play_numbers, check_numbers;
    // cout << str << endl;
    start_base =  str.find(":") + 2;
    start_check =  str.find("|");
    
    play_string = str.substr(start_base,start_check-start_base-1);
    check_string = str.substr(start_check+2);
    
    play_numbers = FindIntString(play_string);
    check_numbers = FindIntString(check_string);
    
    for(const int& i : play_numbers)
        if(count(check_numbers.begin(), check_numbers.end(), i) > 0){
            if (score == 0){
                score++;
            }
            else{
                score *= 2;
            }
        }

    // cout << score << endl;

    // stringstream ss;
    // ss << play_string;
	// string temp;
    // int number;
    // while (!ss.eof()){
	// 	ss >> temp;
    //     if (check_string.find(temp) !=string::npos){
    //         if (score == 0){
    //         score++;
    //         }
    //         else{
    //         score *= 2;
    //         }
    //     }
    // }
    // cout << score << endl;
    return score;
}

int main(){
    SetPath();
    vector<string> data_example, data; 
    int points_example = 0;
	data_example = TXTtoVector("data/day4_example.txt");
	data = TXTtoVector("data/day4.txt");
    for(const string& i : data_example)
        points_example += FindPoints(i);

    cout << "Example answer = " << points_example << endl;
    int points = 0;
    for(const string& i : data)
        points += FindPoints(i);
        cout << "Day answer = " << points << endl;

    return 0;
}
