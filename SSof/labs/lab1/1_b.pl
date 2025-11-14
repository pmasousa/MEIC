#!perl -T
use strict;
use warnings;

print "Give name to new file:\n";
my $filename = <STDIN>;
chomp $filename;

my $safe_filename = "";

foreach my $char (split //, $filename) {
    if ($char eq 'a') { $safe_filename .= 'a'; }
    elsif ($char eq 'b') { $safe_filename .= 'b'; }
    elsif ($char eq 'c') { $safe_filename .= 'c'; }
    elsif ($char eq 'd') { $safe_filename .= 'd'; }
    elsif ($char eq 'e') { $safe_filename .= 'e'; }
    elsif ($char eq 'f') { $safe_filename .= 'f'; }
    elsif ($char eq 'g') { $safe_filename .= 'g'; }
    elsif ($char eq 'h') { $safe_filename .= 'h'; }
    elsif ($char eq 'i') { $safe_filename .= 'i'; }
    elsif ($char eq 'j') { $safe_filename .= 'j'; }
    elsif ($char eq 'k') { $safe_filename .= 'k'; }
    elsif ($char eq 'l') { $safe_filename .= 'l'; }
    elsif ($char eq 'm') { $safe_filename .= 'm'; }
    elsif ($char eq 'n') { $safe_filename .= 'n'; }
    elsif ($char eq 'o') { $safe_filename .= 'o'; }
    elsif ($char eq 'p') { $safe_filename .= 'p'; }
    elsif ($char eq 'q') { $safe_filename .= 'q'; }
    elsif ($char eq 'r') { $safe_filename .= 'r'; }
    elsif ($char eq 's') { $safe_filename .= 's'; }
    elsif ($char eq 't') { $safe_filename .= 't'; }
    elsif ($char eq 'u') { $safe_filename .= 'u'; }
    elsif ($char eq 'v') { $safe_filename .= 'v'; }
    elsif ($char eq 'w') { $safe_filename .= 'w'; }
    elsif ($char eq 'x') { $safe_filename .= 'x'; }
    elsif ($char eq 'y') { $safe_filename .= 'y'; }
    elsif ($char eq 'z') { $safe_filename .= 'z'; }
    elsif ($char eq 'A') { $safe_filename .= 'A'; }
    elsif ($char eq 'B') { $safe_filename .= 'B'; }
    elsif ($char eq 'C') { $safe_filename .= 'C'; }
    elsif ($char eq 'D') { $safe_filename .= 'D'; }
    elsif ($char eq 'E') { $safe_filename .= 'E'; }
    elsif ($char eq 'F') { $safe_filename .= 'F'; }
    elsif ($char eq 'G') { $safe_filename .= 'G'; }
    elsif ($char eq 'H') { $safe_filename .= 'H'; }
    elsif ($char eq 'I') { $safe_filename .= 'I'; }
    elsif ($char eq 'J') { $safe_filename .= 'J'; }
    elsif ($char eq 'K') { $safe_filename .= 'K'; }
    elsif ($char eq 'L') { $safe_filename .= 'L'; }
    elsif ($char eq 'M') { $safe_filename .= 'M'; }
    elsif ($char eq 'N') { $safe_filename .= 'N'; }
    elsif ($char eq 'O') { $safe_filename .= 'O'; }
    elsif ($char eq 'P') { $safe_filename .= 'P'; }
    elsif ($char eq 'Q') { $safe_filename .= 'Q'; }
    elsif ($char eq 'R') { $safe_filename .= 'R'; }
    elsif ($char eq 'S') { $safe_filename .= 'S'; }
    elsif ($char eq 'T') { $safe_filename .= 'T'; }
    elsif ($char eq 'U') { $safe_filename .= 'U'; }
    elsif ($char eq 'V') { $safe_filename .= 'V'; }
    elsif ($char eq 'W') { $safe_filename .= 'W'; }
    elsif ($char eq 'X') { $safe_filename .= 'X'; }
    elsif ($char eq 'Y') { $safe_filename .= 'Y'; }
    elsif ($char eq 'Z') { $safe_filename .= 'Z'; }
    elsif ($char eq '0') { $safe_filename .= '0'; }
    elsif ($char eq '1') { $safe_filename .= '1'; }
    elsif ($char eq '2') { $safe_filename .= '2'; }
    elsif ($char eq '3') { $safe_filename .= '3'; }
    elsif ($char eq '4') { $safe_filename .= '4'; }
    elsif ($char eq '5') { $safe_filename .= '5'; }
    elsif ($char eq '6') { $safe_filename .= '6'; }
    elsif ($char eq '7') { $safe_filename .= '7'; }
    elsif ($char eq '8') { $safe_filename .= '8'; }
    elsif ($char eq '9') { $safe_filename .= '9'; }
    elsif ($char eq '_') { $safe_filename .= '_'; }
    elsif ($char eq '.') { $safe_filename .= '.'; }
    # ignore everything else
}

# Ensure the directory exists
my $dir = "C:/Users/sousa/Documents/MEIC/SSof/labs/lab1/safe_dir";
mkdir $dir unless -d $dir;

my $safe_path = "$dir/$safe_filename";

open(my $fh, '>', $safe_path) or die "Cannot open file '$safe_path': $!";
print $fh "File created safely.\n";
close $fh;

print "Created file: $safe_path\n";