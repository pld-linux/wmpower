Summary:	Dockable APM/ACPI monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM/ACPI dla WindowMakera
Summary(pt_BR):	Aplicativo do dock do WindowMaker para monitorar a carga da bateria
Summary(es):	Una aplicación para monitorar la batería en el dock del WindowMaker
Name:		wmpower
Version:	0.3.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	0c867f3b2a1746a1d423bf517f1fc316
Source1:	%{name}.desktop
URL:		http://wmpower.sourceforge.net/
BuildRequires:	XFree86-devel
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmpower is a WindowMaker dock application allowing the user to graphically
see the power management status of his laptop.

%description -l pl
wmpower jest aplikacj± dokuj±c± dla WindowMakera, pozwalaj±c±
u¿ytkownikowi zwizualizowaæ ustawienia zarz±dzania energi± swojego
laptopa.

%description -l pt_BR
Aplicativo do dock do WindowMaker para monitorar a carga da bateria,
através do suporte APM/ACPI do kernel. Esta informação é útil para
usuários de laptops.

%description -l es
Aplicación para monitorar la batería en el dock del WindowMaker.
Basado en soporte APM/ACPI del kernel. Es útil en notebooks.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/*
