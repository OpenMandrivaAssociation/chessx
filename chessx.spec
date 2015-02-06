Name:		chessx
Version:	0.8
Release:	2
Summary:	An Open Source chess database
License:	GPLv2
Group:		Games/Boards
URL:		http://chessx.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel

%description
ChessX is an Open Source chess database. With ChessX you can operate on your
collection of chess games in many ways:
browse, edit, add, organize, analyze, etc.

%prep
%setup -q

%build
%qmake_qt4

# building language files
/usr/lib/qt4/bin/lrelease i18n/*.ts

%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesbindir}
install -m0755 bin/chessx %{buildroot}%{_gamesbindir}

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
cp -r data/* %{buildroot}%{_gamesdatadir}/%{name}

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}/lang
cp i18n/*.qm %{buildroot}%{_gamesdatadir}/%{name}/lang/


#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=ChessX
Comment=Open Source chess database
Exec=%{name}
Icon=strategy_section
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%files
%defattr(-,root,root,0755)
%doc COPYING ChangeLog
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}




%changelog
* Mon Nov 28 2011 Andrey Bondrov <abondrov@mandriva.org> 0.8-1mdv2011.0
+ Revision: 734931
- imported package chessx

