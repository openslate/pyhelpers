
Welcome to pyhelpers's documentation!
*************************************

**pyhelpers.chunk_generator(_list, size)**

   Generator yielding chunks of *_list* with *size* members

**pyhelpers.cron(spec, dt=None)**

   test if the cronspec specified by spec matches the time passed as
   dt or now

**pyhelpers.cron_daynumber(day)**

   translate word days into cron day number

**pyhelpers.cron_to_python_daynumber(d)**

   cron day number to stupid python day number cron: Sunday: 0 -
   Saturday: 6 python: Monday: 0 - Sunday: 6

**pyhelpers.dict_path(dct, k, default=None)**

   Turns dotted 'path' into dict key. snippet.thumbnails.default ->
   dct['snippet']['thumbnails']['default']

**pyhelpers.dotkeys(dct, prefix=None)**

   return list of (key, value) for everything in dct where key is the
   'dict_path'-style dotted name

**pyhelpers.parse_cron(spec)**

   turns a cronspec string (eg. 12 4 * * *) into a dict

**pyhelpers.set_interval(interval)**

   Call decorated funtion every *interval* seconds

**pyhelpers.write_dict_path(dct, k, value)**

   set dict_path(dct, k) to value

**pyhelpers.progbar.progbar(t, c=None)**

   Draw progress bar of t/100 across screen width c
