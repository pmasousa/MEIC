#!perl -T
use strict;
use warnings;

print "Give name to new file:\n";
my $filename = <STDIN>;
chomp $filename;

if ($filename =~ /^([-\@\w.]+)$/) {  # untaint
    $filename = $1;
} else {
    die "Boo! Invalid filename.\n";    # input rejected
}

# Prepend a safe path
my $safe_path = "C:/Users/sousa/Documents/MEIC/SSof/labs/lab1/safe_dir/$filename";

# Make sure directory exists
my $dir = "C:/Users/sousa/Documents/MEIC/SSof/labs/lab1/safe_dir";
mkdir $dir unless -d $dir;

open(my $fh, '>', $safe_path) or die "Cannot open file '$safe_path': $!";
print $fh "File created safely.\n";
close $fh;

print "Created file: $safe_path\n";
