Name:           gamescope-session-steam
Version:        0.2.git.201.5538cd66
Release:        42%{?dist}
Summary:        Steam Deck Mode session

License:        MIT
URL:            https://github.com/nobara-project/steamdeck-edition-packages
Source0:        %{URL}/releases/download/1.0/gamescope-session-steam.tar.gz
Source1:        https://large-package-sources.nobaraproject.org/steam-bootstrap.tar.gz

BuildArch:      noarch

Requires:       gamescope-session-plus
Requires:       gamescope
Requires:       edid-decode
Requires:       python3
Requires:       pulseaudio-utils
Requires:       steam-powerbuttond
Requires:       steam

BuildRequires:  systemd-rpm-macros

%description
Steam Deck Mode session

# Disable debug packages
%define debug_package %{nil}

%prep
tar -xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_datadir}/gamescope-session-plus/
mkdir -p %{buildroot}%{_libexecdir}/
mkdir -p %{buildroot}%{_sysconfdir}/skel/Desktop/
cp -rv gamescope-session-steam/usr/bin/* %{buildroot}%{_bindir}
cp -rv gamescope-session-steam/usr/share/* %{buildroot}%{_datadir}
cp -rf gamescope-session-steam/usr/libexec/* %{buildroot}%{_libexecdir}/
cp -rv gamescope-session-steam/etc/* %{buildroot}%{_sysconfdir}
mv gamescope-session-steam/LICENSE .
mv %{SOURCE1} %{buildroot}%{_datadir}/gamescope-session-plus/

# Do post-installation
%post
# steam bootstrap needed for gamescope-session first-run
mkdir -p %{_sysconfdir}/skel/.local/share/
tar -xf %{_datadir}/gamescope-session-plus/steam-bootstrap.tar.gz -C %{_sysconfdir}/skel/.local/share/

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%{_bindir}/steam-http-loader
%{_bindir}/steamos-select-branch
%{_bindir}/steamos-session-select
%{_bindir}/steamos-desktop-return
%{_bindir}/steamos-update
%{_datadir}/applications/gamescope-mimeapps.list
%{_datadir}/applications/steam_http_loader.desktop
%{_datadir}/gamescope-session-plus/sessions.d/steam
%{_datadir}/gamescope-session-plus/steam-bootstrap.tar.gz
%{_datadir}/polkit-1/actions/org.nobaraproject.update.policy
%{_datadir}/polkit-1/actions/org.nobaraproject.session.select.policy
%{_datadir}/wayland-sessions/gamescope-session-steam.desktop
%{_datadir}/icons/hicolor/scalable/actions/*
%{_datadir}/icons/hicolor/scalable/places/*
%{_sysconfdir}/xdg/autostart/steam.desktop
%{_sysconfdir}/skel/Desktop/Return.desktop
%{_sysconfdir}/skel/Desktop/steam-with-controls.desktop
%{_libexecdir}/os-session-select

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}
