Summary:	Simple Hangul X Input Method
Name:		nabi
Version:	0.99.7
Release:	%mkrel 2
Group:		System/Internationalization
License:	GPLv2
URL:		http://nabi.kldp.net
Source:		http://download.kldp.net/%name/Nabi/%version/%name-%version.tar.gz
BuildRequires:	gtk2-devel >= 2.4.0
BuildRequires:	libhangul-devel >= 0.0.6
Requires:	locales-ko
BuildRoot:	%_tmppath/%name-%version-root

%description
Nabi is a simple XIM for Korean, implemented with GTK+2.
It can dock in the notification area, and also show the
status of imhangul (See also http://imhangul.kldp.net).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build
%configure2_5x
%make

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %_bindir/nabi
%_datadir/nabi
%_iconsdir/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.7-2mdv2011.0
+ Revision: 620429
- the mass rebuild of 2010.0 packages

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix license to gplv2
    - use tar.gz
    - use %%configure2_5x and %%make
    - update to 0.99.7

* Wed Aug 12 2009 Thierry Vignaud <tv@mandriva.org> 0.99.4-1mdv2010.0
+ Revision: 415386
- new release
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Thierry Vignaud <tv@mandriva.org> 0.99.0-1mdv2008.1
+ Revision: 140637
- new release
- kill re-definition of %%buildroot on Pixel's request
- fix spacing in description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 10 2007 Thierry Vignaud <tv@mandriva.org> 0.19-1mdv2008.1
+ Revision: 96740
- new release
- fix source URL

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2008.1
+ Revision: 80153
- require a newer libhangul
- new release
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.17-1mdv2008.0
+ Revision: 69785
- convert menu to XDG
- buildrequire libhangul-devel
- new release
- Import nabi



* Mon Jul 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-1mdk
- New release 0.15
- mkrel 

* Thu Sep 23 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.14-1mdk
- new release

* Thu Aug 19 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.13-2mdk
- nabi shall request locales-ko

* Fri Jul 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.13-1mdk
- initial release
