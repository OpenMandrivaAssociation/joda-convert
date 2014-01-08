
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		joda-convert
Version:	1.3.1
Release:	2.0
License:	GPLv3+
Source0:	joda-convert-1.3.1-2.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/joda-convert
BuildArch:	noarch
Summary:	joda-convert bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1:1.6
Requires:	jpackage-utils
Provides:	joda-convert = 1.3.1-2.0:2014.0
Provides:	mvn(org.joda:joda-convert) = 1.3.1
Provides:	osgi(joda-convert) = 1.3.1

%description
joda-convert bootstrap version.

%files
/usr/share/doc/joda-convert
/usr/share/doc/joda-convert/LICENSE.txt
/usr/share/doc/joda-convert/NOTICE.txt
/usr/share/doc/joda-convert/RELEASE-NOTES.txt
/usr/share/java/joda-convert.jar
/usr/share/maven-effective-poms/JPP-joda-convert.pom
/usr/share/maven-fragments/joda-convert.xml
/usr/share/maven-poms/JPP-joda-convert.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
