import binary_converter, ascii_converter
import sys

#Don't ask me why, but I did it ok? :)
args = [
    sys.argv[1],
    sys.argv[2]
]


if args[0] == "-b":
    binary_input = args[1]
    ascii_nums = binary_converter.long_conversion(binary_input)
    text = ascii_converter.big_input(ascii_nums)
    print(f"""
        Binary to text:
            Input:          {binary_input}
            Output_ascii:   {ascii_nums} 
            Output:         {text}
""")
elif args[0] == '-t':
    text = args[1]
    t = ascii_converter.text_to_ascii(text)
    b = binary_converter.convert_all_to_binary(t)
    print(f"""
        Text to binary:
            input:          {text}
            ouput_ascii:    {t}
            output:         {b}
    """)





