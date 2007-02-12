Summary:	Dockable APM/ACPI monitor for WindowMaker
Summary(es.UTF-8):	Una aplicación para monitorar la batería en el dock del WindowMaker
Summary(pl.UTF-8):	Dokowalny monitor APM/ACPI dla WindowMakera
Summary(pt_BR.UTF-8):	Aplicativo do dock do WindowMaker para monitorar a carga da bateria
Name:		wmpower
Version:	0.4.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmpower/%{name}-%{version}.tar.bz2
# Source0-md5:	b0dd1629a8d8c913d0da6b5da2ba9581
Source1:	%{name}.desktop
Patch0:		%{name}-asneeded.patch
URL:		http://wmpower.sourceforge.net/
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xextproto-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmpower is a WindowMaker dock application allowing the user to graphically
see the power management status of his laptop.

%description -l pl.UTF-8
wmpower jest aplikacją dokującą dla WindowMakera, pozwalającą
użytkownikowi zwizualizować ustawienia zarządzania energią swojego
laptopa.

%description -l pt_BR.UTF-8
Aplicativo do dock do WindowMaker para monitorar a carga da bateria,
através do suporte APM/ACPI do kernel. Esta informação é útil para
usuários de laptops.

%description -l es.UTF-8
Aplicación para monitorar la batería en el dock del WindowMaker.
Basado en soporte APM/ACPI del kernel. Es útil en notebooks.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc AUTHORS ChangeLog README* THANKS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/*
