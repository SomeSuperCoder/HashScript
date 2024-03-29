from Values import *

global_symbol_table = SymbolTable()
global_symbol_table.set("None", Number.null)
global_symbol_table.set("False", Number.false)
global_symbol_table.set("True", Number.true)
global_symbol_table.set("pi", Number.math_PI)
global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("print_ret", BuiltInFunction.print_ret)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("input_num", BuiltInFunction.input_num)
global_symbol_table.set("is_number", BuiltInFunction.is_number)
global_symbol_table.set("is_string", BuiltInFunction.is_string)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_fun", BuiltInFunction.is_function)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("len", BuiltInFunction.len)
global_symbol_table.set("to_number", BuiltInFunction.to_number)
global_symbol_table.set("to_string", BuiltInFunction.to_string)
