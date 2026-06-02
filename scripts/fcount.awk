#!/bin/awk -f

# Analyse rate of changes of the mapserver filesystem. The output only makes
# sense when files are immutable. I.e. after a file was created, it is
# never modified or removed.
#
# Input must have at least three fields on each line:
#	size	xxx	mtime
# Lines that do not start with a number are ignored.
# The "size" field is the size of the file in bytes.
# The "mtime" field is the time of last modification of the file in epoch.
# The second field is ignored, as are any fields after the third one.
#
# That can be generated with something like this:
#	find /the/file/system/ -type f -printf '%s %C@ %T@ %p\n'
#
# The "cutoff" variable can be set to ignore files older than specified.
# This can be set like this:
#	-v cutoff=$(date +%s --date=2024-01-01)

BEGIN {
	cutoff = length(cutoff) ? cutoff : 0;
	now = systime();
	earliest = now;
}

/^[0-9]/ && $3 > cutoff {
	files++;
	total_size += $1;
	if (earliest > $3) {
		earliest = $3;
	}
}

END {
	printf("files count: %d\n", files);
	printf("total size: ~%d TiB\n", total_size/(1024*1024*1024*1024));
	printf("average size: %d\n", total_size / files);

	months = (now - earliest)/(60*60*24*30)
	printf("~%.2f months since %s\n", months, strftime("%c", earliest));

	printf("~%d files per month\n", files/months);
	printf("~%.2f GiB per month\n", total_size/months/(1024*1024*1024));
}
