#include <vector>
#include <fstream>
#include <iostream>
#include <filesystem>
#include <sstream>
#include <bits/stdc++.h>
#include <ranges>


#include "c_lib.h"

using namespace std;

class PartOne: public BaseAdventofcode {
    public:

    string path_name = "unset";
    int score = 0;
    vector<string> data;

    void Run(){
        this->data = TXTtoVector(this->path_name);
        for(const string& i : this->data)
            this->FindPoints(i);
        cout << "for " << this->path_name << " output is: " << this->score << endl;
    }


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

    void FindPoints(string str){
        int start_base, start_check, score=0; 
        string play_string, check_string;
        vector<int> play_numbers, check_numbers;

        start_base =  str.find(":") + 2;
        start_check =  str.find("|");
        
        play_string = str.substr(start_base,start_check-start_base-1);
        check_string = str.substr(start_check+2);
        
        play_numbers = this->FindIntString(play_string);
        check_numbers = this->FindIntString(check_string);
        
        for(const int& i : play_numbers)
            if(count(check_numbers.begin(), check_numbers.end(), i) > 0){
                if (score == 0){
                    score++;
                }
                else{
                    score *= 2;
                }
            }
        this->score += score;
    }
};





int main(){
    // SetPath();
    PartOne example, day;
    day.SetPath();

    example.path_name = "data/day4_example.txt";
    example.Run();

    day.path_name = "data/day4.txt";
    day.Run();

    return 0;
}
