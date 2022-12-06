#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <unordered_set>

#define P1

int main()
{
    std::cout << "hello world\n";

    std::ifstream fd{ "day6input.txt" };
    // int sum { 0 };

    if (!fd)
    {
        std::cerr << "file not found\n";
        return 1;
    }

    std::string line;
    std::getline(fd, line);

    const char * line_c_style{ line.c_str() };

#ifdef P1
    const int window_size { 4 };
#else
    const int window_size { 14 };
#endif

    char window[window_size] = { 0 };
    int i{ 0 };

    if (strlen(line_c_style) < 3)
    {
        std::cerr << "mew\n";
        exit(1);
    }

    std::memcpy(window, line_c_style, window_size);

    while (line_c_style[i] != '\n')
    {
        bool unique{ true };
        for (int j=0; j<window_size; j++)
        {
            for(int k=j+1; k<window_size; k++)
            {
                if (window[j] == window[k])
                {
                    unique = false;
                    break;
                }
            }
        }

        if (unique)
        {
            break;
        }

        std::memcpy(window, &(line_c_style[++i]), window_size);
    }

    std::cout << i+window_size << '\n';


    return 0;
}


