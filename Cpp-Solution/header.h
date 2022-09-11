#ifndef MY_HDR
#define MY_HDR
    #include <string>
    #include <vector>
    #include <algorithm>

    namespace Sphesihle{
        class Equation{
            private:
                std::string left, right;
            public:
                Equation(): left(""), right(""){};
                Equation(std::string l , std::string r): right(r), left(l){}

                
        };
    }
#endif