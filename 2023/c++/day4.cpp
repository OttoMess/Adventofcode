#include <iostream>
#include <filesystem>
#include <ranges>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include "c_lib.h"

using namespace std;

class PartOne : public BaseAdventofcode
{
public:
    int score = 0;

    PartOne(string path_name, bool set_path)
    { // constructor runs when the class is made
        if (set_path == true)
        {
            this->SetPath();
        }
        const vector<string> data = TXTtoVector(path_name);
        for (const string &i : data)
            this->FindPoints(i);
        cout << "For " << path_name << " output is: " << this->score << endl;
    }

    void FindPoints(string str)
    {
        int start_base, start_check, score = 0;
        string play_string, check_string;
        vector<int> play_numbers, check_numbers;

        start_base = str.find(":");
        start_check = str.find("|");

        play_string = str.substr(start_base + 2, start_check - start_base - 1);
        check_string = str.substr(start_check + 2);

        play_numbers = this->FindIntString(play_string);
        check_numbers = this->FindIntString(check_string);

        for (const int &i : play_numbers)
            if (binary_search(check_numbers.begin(), check_numbers.end(), i) == true)
            {
                // if(count(check_numbers.begin(), check_numbers.end(), i) > 0){
                if (score == 0)
                {
                    score++;
                }
                else
                {
                    score *= 2;
                }
            }
        this->score += score;
    }
};

int main()
{

    PartOne("data/day4_example.txt", true);
    PartOne("data/day4.txt", false);

    return 0;
}
