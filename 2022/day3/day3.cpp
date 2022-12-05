#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>


int find_priority(char c)
{
    auto ascii_code = static_cast<int>(c);
    return ascii_code == 0 ? 0 : ascii_code > 90 ? ascii_code - 97 + 1 : ascii_code - 65 + 27;
}

char find_errorneous_item(std::string &s)
{
    if (s != "")
    {
        if (s.length() % 2)
        {
            std::cerr << "error, odd number of items in knapsack\n";
            exit(1);
        }

        std::unordered_set<char> first_compartment;
        for (int i=0; i < s.length()/2; i++)
        {
            first_compartment.insert(s[i]);
        }

        for (int i=s.length()/2; i < s.length(); i++)
        {
            if (first_compartment.find(s[i]) != first_compartment.end())
            {
                // std::cout << "found " << s[i] << '\n';
                return s[i];
            }
        }
    }

    // should never reach here
    return 0;
}

int main()
{
    std::cout << "hello world\n";

    std::ifstream fd{ "day3input.txt" };
    int sum { 0 };

    if (!fd)
    {
        std::cerr << "file not found\n";
        return 1;
    }

    while (fd)
    {
        std::string line;
        std::getline(fd, line);

        sum += find_priority(find_errorneous_item(line));
        // std::cout << find_priority(find_errorneous_item(line)) << "\n";
    }
    std::cout << sum << "\n";

    fd.close();
    return 0;
}
