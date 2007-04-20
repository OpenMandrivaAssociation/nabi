Summary: Simple Hangul X Input Method
Name:   nabi
Version: 0.17
Release: %mkrel 1
Group: System/Internationalization
License: GPL
URL: http://nabi.kldp.net
Source: http://download.kldp.net/%name/%name-%version.tar.bz2
BuildRequires: gtk2-devel >= 2.4.0
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
mkdir -p $RPM_BUILD_ROOT/%_menudir
cat >$RPM_BUILD_ROOT%_menudir/nabi<<EOF
?package(%name): needs="x11" section="More applications/Accessibility" \
         title="Nabi" \
         longtitle="Simple Hangul XIM" \
         command="%_bindir/%name" \
		 icon="%name.png"
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
%_menudir/%name
