#!/usr/bin/env bash

# For relative paths
root_dir=$( dirname $( readlink -f "${0}" ) )

# Redirect stderr
log_file="${root_dir}/pijamo.log"
exec 2> "${log_file}"

# Get a list of all files to process
export files=$( find "${1}" -type f -name "*.m4a" )

# Count the total number of files
total=$( echo "${files}" | wc -l )

# For pijamo's Python script
. "${root_dir}/env/bin/activate"

# Use as the forloop's delimiter
IFS=$'\n'

current=0
for file in ${files}
do
    current_terminal_width=$( tput cols )

    (( max_filename_size=${current_terminal_width}
	-`echo ${current} | wc -m`
	-`echo ${totam} | wc -m`
	-10 ))

    trunc_filename=$( echo "${file}" | cut -c1-${max_filename_size} )

    (( current=$current+1 ))
    echo -ne "\r\033[2K${current}/${total} ${trunc_filename}..."
    python "${root_dir}/pijamo" "${file}" "${2}"
    exit_code=${?}
    if [ ${exit_code} -ne 0 ]
    then
	echo -e "\r\033[2KExit code: ${exit_code}"
	echo "Log file: ${log_file}"
	exit ${exit_code}
    fi
done

echo -e "\r\033[2KFiles processing succeeded."
exit 0
