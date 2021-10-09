#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flac
Version  : 1.3.3
Release  : 36
URL      : http://downloads.xiph.org/releases/flac/flac-1.3.3.tar.xz
Source0  : http://downloads.xiph.org/releases/flac/flac-1.3.3.tar.xz
Summary  : Free Lossless Audio Codec Library
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: flac-bin = %{version}-%{release}
Requires: flac-filemap = %{version}-%{release}
Requires: flac-lib = %{version}-%{release}
Requires: flac-license = %{version}-%{release}
Requires: flac-man = %{version}-%{release}
BuildRequires : docbook-utils
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : nasm-bin

%description
/* FLAC - Free Lossless Audio Codec
*
* This file is part the FLAC project.  FLAC is comprised of several
* components distributed under different licenses.  The codec libraries
* are distributed under Xiph.Org's BSD-like license (see the file
* COPYING.Xiph in this distribution).  All other programs, libraries, and
* plugins are distributed under the LGPL or GPL (see COPYING.LGPL and
* COPYING.GPL).  The documentation is distributed under the Gnu FDL (see
* COPYING.FDL).  Each file in the FLAC distribution contains at the top the
* terms under which it may be distributed.
*
* Since this particular file is relevant to all components of FLAC,
* it may be distributed under the Xiph.Org license, which is the least
* restrictive of those mentioned above.  See the file COPYING.Xiph in this
* distribution.
*/

%package bin
Summary: bin components for the flac package.
Group: Binaries
Requires: flac-license = %{version}-%{release}
Requires: flac-filemap = %{version}-%{release}

%description bin
bin components for the flac package.


%package dev
Summary: dev components for the flac package.
Group: Development
Requires: flac-lib = %{version}-%{release}
Requires: flac-bin = %{version}-%{release}
Provides: flac-devel = %{version}-%{release}
Requires: flac = %{version}-%{release}

%description dev
dev components for the flac package.


%package dev32
Summary: dev32 components for the flac package.
Group: Default
Requires: flac-lib32 = %{version}-%{release}
Requires: flac-bin = %{version}-%{release}
Requires: flac-dev = %{version}-%{release}

%description dev32
dev32 components for the flac package.


%package doc
Summary: doc components for the flac package.
Group: Documentation
Requires: flac-man = %{version}-%{release}

%description doc
doc components for the flac package.


%package filemap
Summary: filemap components for the flac package.
Group: Default

%description filemap
filemap components for the flac package.


%package lib
Summary: lib components for the flac package.
Group: Libraries
Requires: flac-license = %{version}-%{release}
Requires: flac-filemap = %{version}-%{release}

%description lib
lib components for the flac package.


%package lib32
Summary: lib32 components for the flac package.
Group: Default
Requires: flac-license = %{version}-%{release}

%description lib32
lib32 components for the flac package.


%package license
Summary: license components for the flac package.
Group: Default

%description license
license components for the flac package.


%package man
Summary: man components for the flac package.
Group: Default

%description man
man components for the flac package.


%prep
%setup -q -n flac-1.3.3
cd %{_builddir}/flac-1.3.3
pushd ..
cp -a flac-1.3.3 build32
popd
pushd ..
cp -a flac-1.3.3 buildavx2
popd
pushd ..
cp -a flac-1.3.3 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633748859
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1633748859
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flac
cp %{_builddir}/flac-1.3.3/COPYING.FDL %{buildroot}/usr/share/package-licenses/flac/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/flac-1.3.3/COPYING.GPL %{buildroot}/usr/share/package-licenses/flac/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/flac-1.3.3/COPYING.LGPL %{buildroot}/usr/share/package-licenses/flac/caeb68c46fa36651acf592771d09de7937926bb3
cp %{_builddir}/flac-1.3.3/COPYING.Xiph %{buildroot}/usr/share/package-licenses/flac/969c976617ec52d93cd04778e9613edb7b596a20
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd ../buildavx512/
%make_install_v4
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flac
/usr/bin/metaflac
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/FLAC++/all.h
/usr/include/FLAC++/decoder.h
/usr/include/FLAC++/encoder.h
/usr/include/FLAC++/export.h
/usr/include/FLAC++/metadata.h
/usr/include/FLAC/all.h
/usr/include/FLAC/assert.h
/usr/include/FLAC/callback.h
/usr/include/FLAC/export.h
/usr/include/FLAC/format.h
/usr/include/FLAC/metadata.h
/usr/include/FLAC/ordinals.h
/usr/include/FLAC/stream_decoder.h
/usr/include/FLAC/stream_encoder.h
/usr/lib64/libFLAC++.so
/usr/lib64/libFLAC.so
/usr/lib64/pkgconfig/flac++.pc
/usr/lib64/pkgconfig/flac.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libFLAC++.so
/usr/lib32/libFLAC.so
/usr/lib32/pkgconfig/32flac++.pc
/usr/lib32/pkgconfig/32flac.pc
/usr/lib32/pkgconfig/flac++.pc
/usr/lib32/pkgconfig/flac.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/flac/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-flac

%files lib
%defattr(-,root,root,-)
/usr/lib64/libFLAC++.so.6
/usr/lib64/libFLAC++.so.6.3.0
/usr/lib64/libFLAC.so.8
/usr/lib64/libFLAC.so.8.3.0
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libFLAC++.so.6
/usr/lib32/libFLAC++.so.6.3.0
/usr/lib32/libFLAC.so.8
/usr/lib32/libFLAC.so.8.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flac/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/flac/969c976617ec52d93cd04778e9613edb7b596a20
/usr/share/package-licenses/flac/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/flac/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/flac.1
/usr/share/man/man1/metaflac.1
