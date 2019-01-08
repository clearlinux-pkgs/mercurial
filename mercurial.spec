#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9C9DC824AA5BDD5 (raf@durin42.com)
#
Name     : mercurial
Version  : 4.8.2
Release  : 11
URL      : https://www.mercurial-scm.org/release/mercurial-4.8.2.tar.gz
Source0  : https://www.mercurial-scm.org/release/mercurial-4.8.2.tar.gz
Source99 : https://www.mercurial-scm.org/release/mercurial-4.8.2.tar.gz.asc
Summary  : Fast scalable distributed SCM (revision control, version control) system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ MIT Python-2.0 ZPL-2.1
Requires: mercurial-bin = %{version}-%{release}
Requires: mercurial-data = %{version}-%{release}
Requires: mercurial-libexec = %{version}-%{release}
Requires: mercurial-license = %{version}-%{release}
Requires: mercurial-man = %{version}-%{release}
Requires: mercurial-python = %{version}-%{release}
Requires: mercurial-legacypython
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : docutils-legacypython
BuildRequires : gcc
BuildRequires : gettext
BuildRequires : python-dev
BuildRequires : setuptools-legacypython
BuildRequires : sqlite-autoconf-dev
BuildRequires : subversion
Patch1: mercurial-locale-path-fix.patch
Patch2: hgk-path-fix.patch
Patch3: stateless.patch

%description
Mercurial is a fast, lightweight source control management system designed
for efficient handling of very large distributed projects.

%package bin
Summary: bin components for the mercurial package.
Group: Binaries
Requires: mercurial-data = %{version}-%{release}
Requires: mercurial-libexec = %{version}-%{release}
Requires: mercurial-license = %{version}-%{release}
Requires: mercurial-man = %{version}-%{release}

%description bin
bin components for the mercurial package.


%package data
Summary: data components for the mercurial package.
Group: Data

%description data
data components for the mercurial package.


%package legacypython
Summary: legacypython components for the mercurial package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the mercurial package.


%package libexec
Summary: libexec components for the mercurial package.
Group: Default
Requires: mercurial-license = %{version}-%{release}

%description libexec
libexec components for the mercurial package.


%package license
Summary: license components for the mercurial package.
Group: Default

%description license
license components for the mercurial package.


%package man
Summary: man components for the mercurial package.
Group: Default

%description man
man components for the mercurial package.


%package python
Summary: python components for the mercurial package.
Group: Default

%description python
python components for the mercurial package.


%prep
%setup -q -n mercurial-4.8.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
sed -i 's|python|python2|' %{_builddir}/%{name}-4.8*/Makefile %{_builddir}/%{name}-4.8*/doc/Makefile
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546959239
make  %{?_smp_mflags} all PREFIX=%{_usr} PYTHON=python2


%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests && /usr/bin/python2 run-tests.py --local test-s*

%install
export SOURCE_DATE_EPOCH=1546959239
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mercurial
cp COPYING %{buildroot}/usr/share/package-licenses/mercurial/COPYING
cp contrib/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/mercurial/contrib_packaging_debian_copyright
cp contrib/python-zstandard/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/contrib_python-zstandard_LICENSE
cp contrib/python-zstandard/zstd/COPYING %{buildroot}/usr/share/package-licenses/mercurial/contrib_python-zstandard_zstd_COPYING
cp contrib/python-zstandard/zstd/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/contrib_python-zstandard_zstd_LICENSE
cp contrib/wix/COPYING.rtf %{buildroot}/usr/share/package-licenses/mercurial/contrib_wix_COPYING.rtf
cp i18n/polib.LICENSE %{buildroot}/usr/share/package-licenses/mercurial/i18n_polib.LICENSE
cp mercurial/thirdparty/attr/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/mercurial_thirdparty_attr_LICENSE.txt
cp mercurial/thirdparty/cbor/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/mercurial_thirdparty_cbor_LICENSE.txt
cp mercurial/thirdparty/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/mercurial_thirdparty_concurrent_LICENSE
cp mercurial/thirdparty/zope/interface/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/mercurial_thirdparty_zope_interface_LICENSE.txt
%make_install PREFIX=%{_usr} PYTHON=python2
## install_append content
install -Dm0755 contrib/hgk %{buildroot}%{_libexecdir}/mercurial/hgk
install -m0755 contrib/hg-ssh %{buildroot}%{_bindir}
install -Dm0644 contrib/bash_completion %{buildroot}%{_datadir}/bash-completion/completions/hg
install -Dm0644 contrib/zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_mercurial
mkdir -p %{buildroot}%{_datadir}/{x,}emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/xemacs/site-lisp
cat >hgk.rc <<EOF
[extensions]
hgk=
[hgk]
path=%{_libexecdir}/mercurial/hgk
EOF
install -Dm0644 hgk.rc %{buildroot}%{_datadir}/defaults/mercurial/hgrc.d/hgk.rc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hg
/usr/bin/hg-ssh

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/hg
/usr/share/defaults/mercurial/hgrc.d/hgk.rc
/usr/share/emacs/site-lisp/hg-test-mode.el
/usr/share/emacs/site-lisp/mercurial.el
/usr/share/emacs/site-lisp/mq.el
/usr/share/xemacs/site-lisp/hg-test-mode.el
/usr/share/xemacs/site-lisp/mercurial.el
/usr/share/xemacs/site-lisp/mq.el
/usr/share/zsh/site-functions/_mercurial

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mercurial/hgk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mercurial/COPYING
/usr/share/package-licenses/mercurial/contrib_packaging_debian_copyright
/usr/share/package-licenses/mercurial/contrib_python-zstandard_LICENSE
/usr/share/package-licenses/mercurial/contrib_python-zstandard_zstd_COPYING
/usr/share/package-licenses/mercurial/contrib_python-zstandard_zstd_LICENSE
/usr/share/package-licenses/mercurial/contrib_wix_COPYING.rtf
/usr/share/package-licenses/mercurial/i18n_polib.LICENSE
/usr/share/package-licenses/mercurial/mercurial_thirdparty_attr_LICENSE.txt
/usr/share/package-licenses/mercurial/mercurial_thirdparty_cbor_LICENSE.txt
/usr/share/package-licenses/mercurial/mercurial_thirdparty_concurrent_LICENSE
/usr/share/package-licenses/mercurial/mercurial_thirdparty_zope_interface_LICENSE.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hg.1
/usr/share/man/man5/hgignore.5
/usr/share/man/man5/hgrc.5
/usr/share/man/man8/hg-ssh.8

%files python
%defattr(-,root,root,-)
