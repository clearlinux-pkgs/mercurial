#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A33DE460D9EC39F (7895pulkit@gmail.com)
#
Name     : mercurial
Version  : 6.0
Release  : 54
URL      : https://www.mercurial-scm.org/release/mercurial-6.0.tar.gz
Source0  : https://www.mercurial-scm.org/release/mercurial-6.0.tar.gz
Source1  : https://www.mercurial-scm.org/release/mercurial-6.0.tar.gz.asc
Source2  : hgk.rc
Summary  : Fast scalable distributed SCM (revision control, version control) system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ MIT Python-2.0 ZPL-2.1
Requires: mercurial-bin = %{version}-%{release}
Requires: mercurial-data = %{version}-%{release}
Requires: mercurial-libexec = %{version}-%{release}
Requires: mercurial-license = %{version}-%{release}
Requires: mercurial-man = %{version}-%{release}
Requires: mercurial-python = %{version}-%{release}
Requires: mercurial-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : gcc
BuildRequires : gettext
BuildRequires : pypi(asn1crypto)
BuildRequires : pypi(bcrypt)
BuildRequires : pypi(bleach)
BuildRequires : pypi(boto3)
BuildRequires : pypi(botocore)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(chardet)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(docutils)
BuildRequires : pypi(idna)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jmespath)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(ntlm_auth)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(persistent)
BuildRequires : pypi(pkginfo)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(pypsrp)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(readme_renderer)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_toolbelt)
BuildRequires : pypi(s3transfer)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(tqdm)
BuildRequires : pypi(twine)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(webencodings)
BuildRequires : pypi(wheel)
BuildRequires : python3-dev
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

%description bin
bin components for the mercurial package.


%package data
Summary: data components for the mercurial package.
Group: Data

%description data
data components for the mercurial package.


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
Requires: mercurial-python3 = %{version}-%{release}

%description python
python components for the mercurial package.


%package python3
Summary: python3 components for the mercurial package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mercurial package.


%prep
%setup -q -n mercurial-6.0
cd %{_builddir}/mercurial-6.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
export HGPYTHON3=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641602356
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  all PREFIX=%{_usr} PYTHON=python3


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests && /usr/bin/python3 run-tests.py --local test-s* || :

%install
export SOURCE_DATE_EPOCH=1641602356
rm -rf %{buildroot}
## install_prepend content
export HGPYTHON3=1
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/mercurial
cp %{_builddir}/mercurial-6.0/COPYING %{buildroot}/usr/share/package-licenses/mercurial/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/mercurial-6.0/contrib/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/mercurial/a6910991bf1d49c1989a4b11ce2efd2ec57a830e
cp %{_builddir}/mercurial-6.0/contrib/python-zstandard/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/bdfd20ae0e3f88b5609da6191fbb89f33933d948
cp %{_builddir}/mercurial-6.0/contrib/python-zstandard/zstd/COPYING %{buildroot}/usr/share/package-licenses/mercurial/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/mercurial-6.0/contrib/python-zstandard/zstd/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
cp %{_builddir}/mercurial-6.0/i18n/polib.LICENSE %{buildroot}/usr/share/package-licenses/mercurial/f82bb0ed21661ead2ef217c636e572ac55fad68b
cp %{_builddir}/mercurial-6.0/mercurial/thirdparty/attr/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/00ff890e8493d10b07d5d3fafa23639bb071e443
cp %{_builddir}/mercurial-6.0/mercurial/thirdparty/cbor/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/a51ccdcb7a9d8c2116d1dfc16f11b3c8a5830f67
cp %{_builddir}/mercurial-6.0/mercurial/thirdparty/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/mercurial/317697855104f4f264a8e8c266b4760991684440
cp %{_builddir}/mercurial-6.0/mercurial/thirdparty/sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/f0197ae0a546d825bcd59ba21034f36272080a4a
cp %{_builddir}/mercurial-6.0/mercurial/thirdparty/zope/interface/LICENSE.txt %{buildroot}/usr/share/package-licenses/mercurial/a0b53f43aab58b46bf79ba756c50771c605ab4c5
%make_install PREFIX=%{_usr} PYTHON=python3
mkdir -p %{buildroot}/usr/share/defaults/mercurial/hgrc.d
install -Dm0644 %{_sourcedir}/hgk.rc %{buildroot}/usr/share/defaults/mercurial/hgrc.d/hgk.rc
## install_append content
install -Dm0755 contrib/hgk %{buildroot}/usr/libexec/mercurial/hgk
install -m0755 contrib/hg-ssh %{buildroot}/usr/bin
install -Dm0644 contrib/bash_completion %{buildroot}/usr/share/bash-completion/completions/hg
install -Dm0644 contrib/zsh_completion %{buildroot}/usr/share/zsh/site-functions/_mercurial
mkdir -p %{buildroot}/usr/share/{x,}emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}/usr/share/emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}/usr/share/xemacs/site-lisp
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

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mercurial/hgk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mercurial/00ff890e8493d10b07d5d3fafa23639bb071e443
/usr/share/package-licenses/mercurial/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/mercurial/317697855104f4f264a8e8c266b4760991684440
/usr/share/package-licenses/mercurial/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/mercurial/a0b53f43aab58b46bf79ba756c50771c605ab4c5
/usr/share/package-licenses/mercurial/a51ccdcb7a9d8c2116d1dfc16f11b3c8a5830f67
/usr/share/package-licenses/mercurial/a6910991bf1d49c1989a4b11ce2efd2ec57a830e
/usr/share/package-licenses/mercurial/bdfd20ae0e3f88b5609da6191fbb89f33933d948
/usr/share/package-licenses/mercurial/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
/usr/share/package-licenses/mercurial/f0197ae0a546d825bcd59ba21034f36272080a4a
/usr/share/package-licenses/mercurial/f82bb0ed21661ead2ef217c636e572ac55fad68b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hg.1
/usr/share/man/man5/hgignore.5
/usr/share/man/man5/hgrc.5
/usr/share/man/man8/hg-ssh.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
