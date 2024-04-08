# kill proocess killmenow 

exec { 'pkill' :
   command  => 'pkill killmenow',
   provider => 'shell',
}
