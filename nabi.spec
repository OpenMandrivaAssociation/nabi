Summary: Simple Hangul X Input Method
Name:   nabi
Version: 0.18
Release: %mkrel 1
Group: System/Internationalization
License: GPL
URL: http://nabi.kldp.net
Source: http://download.kldp.net/%name/%name-%version.tar.bz2
BuildRequires: gtk2-devel >= 2.4.0
BuildRequires: libhangul-devel >= 0.0.6
Requires: locales-ko
BuildRoot: %_tmppath/%name-%version-root

%description
Nabi is a simple XIM for Korean, implemented with GTK+2.
It can dock in the notification area, and also show the
status of imhangul(See also http://imhangul.kldp.net).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build
%configure
make

%install
%makeinstall_std

# menu entry:
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Nabi
Comment=Simple Hangul XIM
Exec=%name
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Settings;Accessibility;X-MandrivaLinux-System-Configuration-GNOME-Accessibility;
EOF

mkdir -p $RPM_BUILD_ROOT%_iconsdir/
install -m 644 nabi.png $RPM_BUILD_ROOT%_iconsdir/

%find_lang %name

%post
%update_menus

%postun
%update_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %_bindir/nabi
%_datadir/nabi
%_iconsdir/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
