if !has('python')
    finish
endif

let g:set_py_path_plugindir = expand('<sfile>:p:h')

function! SetPyPath()
python << endpython

import os
import sys
import vim 
set_py_path_plugindir = vim.eval('g:set_py_path_plugindir') 
sys.path.append(os.path.abspath(set_py_path_plugindir))

from pyutils import utils
utils.add_py_path_recursively(3)

endpython
endfunction
