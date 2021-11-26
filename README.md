# ritl
Relatives Import Tool : How many time I was blocked by relative import problems. This time is over now...

# Installation
```
pip install ritl
```

# Usage

We just need to put :
```
from ritl import relative_import
relative_import.add(__file__)
```
and we can import easily our modules in the same directory of our file. Wherever you execute it.

You can also add more directories, relative to your file directory :
```
relative_import.add(__file__, "../utils")
```

This will allow you to relatively import your modules from other directory in utils

After this, you just have to import your modules
