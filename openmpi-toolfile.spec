### RPM external openmpi-toolfile 1.0
Requires: openmpi

%prep

%build

%install
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/openmpi.xml
<tool name="openmpi" version="@TOOL_VERSION@">
<lib name="mca_common_sm"/>
<lib name="mpi"/>
<lib name="mpi_cxx"/>
<lib name="mpi_f77"/>
<lib name="mpi_f90"/>
<lib name="ompitrace"/>
<lib name="open-pal"/>
<lib name="open-rte"/>
<client>
<environment name="OPENMPI_BASE" default="@TOOL_ROOT@"/>
<environment name="LIBDIR" default="$OPENMPI_BASE/lib"/>
<environment name="INCLUDE" default="$OPENMPI_BASE/include"/>
</client>
<runtime name="PATH" value="$OPENMPI_BASE/bin" type="path"/>
<runtime name="OPAL_PREFIX" value="$OPENMPI_BASE" type="path"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
