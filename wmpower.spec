Summary:	Dockable APM/ACPI monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM/ACPI dla WindowMakera
Summary(pt_BR):	Aplicativo do dock do WindowMaker para monitorar a carga da bateria
Summary(es):	Una aplicaci�n para monitorar la bater�a en el dock del WindowMaker
Name:		wmpower
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	7ba08d0e2cedb38856427db0b4596579
Source1:	%{name}.desktop
URL:		http://wmpower.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmpower is a WindowMaker dock application allowing the user to graphically
see the power management status of his laptop.

%description -l pl
wmpower jest aplikacj� dokuj�c� dla WindowMakera, pozwalaj�c�
u�ytkownikowi zwizualizowa� ustawienia zarz�dzania energi� swojego
laptopa.

%description -l pt_BR
Aplicativo do dock do WindowMaker para monitorar a carga da bateria,
atrav�s do suporte APM/ACPI do kernel. Esta informa��o � �til para
usu�rios de laptops.

%description -l es
Aplicaci�n para monitorar la bater�a en el dock del WindowMaker.
Basado en soporte APM/ACPI del kernel. Es �til en notebooks.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_applnkdir}/DockApplets/*
