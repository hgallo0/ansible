#!/bin/perl

print "ContentType: text/html\n\n";

use DBI;
use DBD::mysql;

$dbname="gateone";
$dbhost="{{ node }}";
$dbuser="{{ user }}";
$dbpass="{{ pass }}";

$dbh = DBI->connect('dbi:mysql:' . $dbname . ":$dbhost:3306", $dbuser, $dbpass) or die "Connection error: $DBI::errstr\n";

print "GateOne Server information\n\n";

#Select the data and display to the browser
my $sth = $dbh->prepare("SELECT * FROM servers");
$sth->execute();
while (my $ref = $sth->fetchrow_hashref()) {
        print " id = $ref->{'id'} \n serverName = $ref->{'name'} \n eth0_interface = $ref->{'eth0'} \n eth1_interface = $ref->{'eth1'} \n online = $ref->{'online'} \n updated = $ref->{'updated'}";
        print "\n\n";
}

$sth->finish();
$dbh->disconnect();
