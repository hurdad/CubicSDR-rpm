Name:           CubicSDR
Version:		%{VERSION}
Release:        1%{?dist}
Summary:        Cross-Platform Software-Defined Radio Application
License:        GNU GPL2
Group:          Applications/Engineering
Url:            http://www.cubicsdr.com/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:	SoapySDR-devel
BuildRequires:	liquid-dsp-devel
BuildRequires:  fftw-devel
BuildRequires:	gtk3-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pulseaudio-libs-devel

%description
Cross-Platform Software-Defined Radio Application

%prep
%setup -n %{name}-%{version}

%build
build_dir=$(pwd)

wget https://github.com/wxWidgets/wxWidgets/releases/download/v3.1.0/wxWidgets-3.1.0.tar.bz2
tar -xvjf wxWidgets-3.1.0.tar.bz2  
cd wxWidgets-3.1.0/
mkdir -p wxWidgets-staticlib
./autogen.sh 
./configure --with-opengl --disable-shared --enable-monolithic --with-libjpeg --with-libtiff --with-libpng --with-zlib --disable-sdltest --enable-unicode --enable-display --enable-propgrid --disable-webkit --disable-webview --disable-webviewwebkit --prefix=$build_dir/wxWidgets-staticlib CXXFLAGS="-std=c++0x"
make %{?_smp_mflags} && make install

cd $build_dir
cmake3 . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DwxWidgets_CONFIG_EXECUTABLE=$build_dir/wxWidgets-staticlib/bin/wx-config
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/CubicSDR
%{_datarootdir}/cubicsdr/*
%{_datarootdir}/applications/CubicSDR.desktop

%changelog

