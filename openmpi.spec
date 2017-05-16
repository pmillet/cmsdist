### RPM external openmpi 2.1.0
Source: http://www.open-mpi.org/software/ompi/v2.1/downloads/%{n}-%{realversion}.tar.gz 
%prep
%setup -q -n %{n}-%{realversion}

sed -i -e 's|#!/usr/bin/perl|#!/usr/bin/env/perl|' ./opal/asm/generate-asm.pl
sed -i -e 's|#!/usr/bin/perl|#!/usr/bin/env/perl|' opal/asm/generate-all-asm.pl
sed -i -e 's|/usr/bin/perl|/usr/bin/env/perl|' ./Doxyfile
sed -i -e 's|/usr/bin/perl|/usr/bin/env/perl|' ./orte/Doxyfile

./configure --prefix=%i --disable-vt 

%build
make %{makeprocesses} 

%install
make install
