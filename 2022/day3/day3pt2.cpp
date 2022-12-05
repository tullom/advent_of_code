#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>


int find_priority(char c)
{
    auto ascii_code = static_cast<int>(c);
    return ascii_code == 0 ? 0 : ascii_code > 90 ? ascii_code - 97 + 1 : ascii_code - 65 + 27;
}

char find_common_item(std::string &elf_one, std::string &elf_two, std::string &elf_three)
{
    if (elf_one != "" && elf_two != "" && elf_three != "")
    {
        std::unordered_set<char> intersection_elf_one_elf_two;
        for (char item : elf_two)
        {
            auto found = elf_one.find(item);
            if (found != std::string::npos)
            {
                intersection_elf_one_elf_two.insert(item);
            }
        }

        for (char item : intersection_elf_one_elf_two)
        {
            auto found = elf_three.find(item);
            if (found != std::string::npos)
            {
                return item;
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
        std::string elf_1;
        std::string elf_2;
        std::string elf_3;
        std::getline(fd, elf_1);
        std::getline(fd, elf_2);
        std::getline(fd, elf_3);

        sum += find_priority(find_common_item(elf_1, elf_2, elf_3));
        // std::cout << find_priority(find_errorneous_item(line)) << "\n";
    }
    std::cout << sum << "\n";

    fd.close();
    return 0;
}
