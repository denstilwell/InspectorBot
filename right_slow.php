<?php

system ("gpio -g mode 12 out");


system ("gpio -g mode 16 out");
system ("gpio -g mode 20 out");
system ("gpio -g mode 21 out");
system ("gpio -g mode 23 out");
system ("gpio -g mode 24 out");

system ("gpio -g write 12 1") ;
system ("gpio -g write 16 0") ;
system ("gpio -g write 20 0") ;
system ("gpio -g write 21 1") ;
sleep ( .5 );
system ("gpio -g write 12 0") ;
system ("gpio -g write 16 0") ;
system ("gpio -g write 20 0") ;
system ("gpio -g write 21 0") ;
?>