# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.29

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zy/works/AFL-Interface/monitor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zy/works/AFL-Interface/monitor/build

# Include any dependencies generated for this target.
include CMakeFiles/AFL_Monitor.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/AFL_Monitor.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/AFL_Monitor.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/AFL_Monitor.dir/flags.make

CMakeFiles/AFL_Monitor.dir/src/App.cpp.o: CMakeFiles/AFL_Monitor.dir/flags.make
CMakeFiles/AFL_Monitor.dir/src/App.cpp.o: /home/zy/works/AFL-Interface/monitor/src/App.cpp
CMakeFiles/AFL_Monitor.dir/src/App.cpp.o: CMakeFiles/AFL_Monitor.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/zy/works/AFL-Interface/monitor/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/AFL_Monitor.dir/src/App.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/AFL_Monitor.dir/src/App.cpp.o -MF CMakeFiles/AFL_Monitor.dir/src/App.cpp.o.d -o CMakeFiles/AFL_Monitor.dir/src/App.cpp.o -c /home/zy/works/AFL-Interface/monitor/src/App.cpp

CMakeFiles/AFL_Monitor.dir/src/App.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/AFL_Monitor.dir/src/App.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/zy/works/AFL-Interface/monitor/src/App.cpp > CMakeFiles/AFL_Monitor.dir/src/App.cpp.i

CMakeFiles/AFL_Monitor.dir/src/App.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/AFL_Monitor.dir/src/App.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/zy/works/AFL-Interface/monitor/src/App.cpp -o CMakeFiles/AFL_Monitor.dir/src/App.cpp.s

# Object files for target AFL_Monitor
AFL_Monitor_OBJECTS = \
"CMakeFiles/AFL_Monitor.dir/src/App.cpp.o"

# External object files for target AFL_Monitor
AFL_Monitor_EXTERNAL_OBJECTS =

AFL_Monitor: CMakeFiles/AFL_Monitor.dir/src/App.cpp.o
AFL_Monitor: CMakeFiles/AFL_Monitor.dir/build.make
AFL_Monitor: /usr/local/lib/oatpp-1.3.0/liboatpp.a
AFL_Monitor: CMakeFiles/AFL_Monitor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/zy/works/AFL-Interface/monitor/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable AFL_Monitor"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/AFL_Monitor.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/AFL_Monitor.dir/build: AFL_Monitor
.PHONY : CMakeFiles/AFL_Monitor.dir/build

CMakeFiles/AFL_Monitor.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/AFL_Monitor.dir/cmake_clean.cmake
.PHONY : CMakeFiles/AFL_Monitor.dir/clean

CMakeFiles/AFL_Monitor.dir/depend:
	cd /home/zy/works/AFL-Interface/monitor/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zy/works/AFL-Interface/monitor /home/zy/works/AFL-Interface/monitor /home/zy/works/AFL-Interface/monitor/build /home/zy/works/AFL-Interface/monitor/build /home/zy/works/AFL-Interface/monitor/build/CMakeFiles/AFL_Monitor.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/AFL_Monitor.dir/depend

