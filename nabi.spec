Summary:	Simple Hangul X Input Method
Name:		nabi
Version:	1.0.0
Release:	1
License:	GPLv2+
Group:		System/Internationalization
URL:		http://code.google.com/p/nabi
Source:		http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	librsvg
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libhangul)
Requires:	locales-ko

%description
Nabi is a simple XIM for Korean, implemented with GTK+2.
It can dock in the notification area, and also show the
status of imhangul (See also http://imhangul.kldp.net).

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/nabi
%{_datadir}/nabi
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# menu entry:
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Nabi
Comment=Simple Hangul XIM
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Settings;Accessibility;
EOF

# Install icons of various sizes
for s in 256 128 96 48 32 22 16 ; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
rsvg-convert -w ${s} -h ${s} \
    %{name}.svg -o \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

%find_lang %{name}

