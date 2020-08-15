Software
========

The MERCURY HPCs run on the CentOS operating system. The default shell for users
is `TCSH <https://www.tcsh.org/>`_ while the root account is set up with
`BASH <https://www.gnu.org/software/bash/>`_.

Directories
-----------
Each user with username ``$USER`` under the group ``$GROUP`` gets a home directory
located in ``/home/$USER`` and a scratch directory in ``/scratch/$GROUP/$USER``.
Programs are installed in ``/usr/local/Dist`` and their corresponding
`module files <https://modules.readthedocs.io/en/latest/modulefile.html>`_
are located in ``/usr/local/Modules/3.2.0/modulefiles`` on Marcy and
``/usr/local/Modules/modulefiles`` on Skylight. Custom system-wide scripts are
located in ``/usr/local/sbin`` and ``/usr/local/Dist/bin``, i.e. the atmospheric
aerosol scripts like ``run-m08hx-mg3s.csh``.

Permissions
-----------
By default, users have full read/write/execute permissions inside their home
directory and read permissions outside their home directory. Certain users have
sudo powers and the superuser has read/write/execute permissions everywhere. Any
maintenance tasks, such as installing new programs, would require root access,
which can be gained by select users using the ``sudo`` command.

Software Installation
---------------------
New software can be installed by the administrator by following the following
general guideline.

    1. Obtain a copy of the new program's source code. Generally, source code are
       distributed as a single compressed file. ``scp`` can be used to transfer the
       source code file to Marcy. If the web address of a repository is known, ``wget``
       can be used to directly download the file to Marcy. Another option is to use
       ``git`` to obtain the source code.
    2. Gain root access, i.e. ``sudo su``.
    3. Copy the source code to ``/usr/local/Dist``.
    4. Follow the installation instructions for the particular program to completion.
    5. Generate a
       `module file <https://modules.readthedocs.io/en/latest/modulefile.html>`_ in
       ``/usr/local/Modules/3.2.10/modulesfiles`` on Marcy or
       ``/usr/local/Modules/modulefiles`` on Skylight. The easiest way to do this is to
       use an existing module file as a template. Any modules that were loaded to
       install the new program must be included in the module file as dependencies.

After these steps, the new program should be listed as an available module. This can
be checked using the command ``module avail``.

.. toctree::
   :maxdepth: 4
   :caption: Contents
