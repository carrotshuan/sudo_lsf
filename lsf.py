#!/usr/bin/python
# coding=utf-8

import os
import sys

ls_command = "ls -al "
lsattr_command = "lsattr "

# 异常退出
def sys_exit_abnormally():
	sys.exit(-1)

# 正常退出
def sys_exit_normally():
	sys.exit(0)

# 校验是否ls等基本命令可正常执行
def check_basic_commands():

	# system_commands = ['ls','lsattr']
	system_commands = ['ls']

	for command in system_commands:
		result = os.popen("which "+command).read()

		if len( result.strip() ) == 0:
			print "System command "+command+" NOT exists! Please check."

			sys_exit_abnormally()


# 获取路径中的所有待显示参数
def get_all_path_args():

	arg_num = len(sys.argv)
	list_args = sys.argv[1:]

	if arg_num == 1:
		os.system( ls_command + str(" ".join(list_args) ) )
		os.system( lsattr_command + str(" ".join(list_args) ) )
		sys_exit_normally()

	else:
		return list_args


# 提供一个路径，显示路径在上层路径下grep的当前路径的情况
def show_split_single_path(split_path):

	split_position = split_path.rfind("/")

	if split_position == 0 and len(split_path) == 1:
		print "split position error."
		sys_exit_abnormally()

	# 分离前后段路径及路径下的文件名
	prefix_path = split_path[0:split_position]
	suffix_name = split_path[split_position+1:]

	if len(prefix_path) == 0:
		prefix_path = "/"

	# print "PATH split:",prefix_path,suffix_name
	os.system(ls_command + prefix_path +" |grep " + suffix_name+"$")


# 显示单个路径信息
def show_single_path(single_path):
	
	elements = single_path.rstrip("/").split("/")
	# 如果是根目录
	if len(elements) == 0:
		os.system(ls_command + "/")
		sys_exit_normally()

	else:

		all_split_paths = []

		for path_length in range(len(elements)): # 获取单个路径对应的整条待显示分路径
			
			if path_length != len(elements)-1:
				all_split_paths.append( "/".join(elements[0:len(elements) - path_length]) )

		# print all_split_paths

		# 递归显示分路径
		for split_path in all_split_paths:
			show_split_single_path(split_path)


# 逐个显示所有文件及路径所在信息
def show_all_paths(paths):

	for single_path in paths:
		show_single_path(single_path)


def main():

	check_basic_commands()

	paths = get_all_path_args()
	show_all_paths(paths)

if __name__ == '__main__':
	main()
