%define oname ruby_parser

Name:       rubygem-%{oname}
Version:    2.0.5
Release:    %mkrel 1
Summary:    A ruby parser written in pure ruby
Group:      Development/Ruby
License:    MIT
URL:        http://parsetree.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(sexp_processor) >= 3.0
Requires:   rubygem(rubyforge) >= 2.0.4
Requires:   rubygem(minitest) >= 1.7.1
Requires:   rubygem(ParseTree) >= 3.0
Requires:   rubygem(hoe) >= 2.6.2
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{oname}) = %{version}

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). RP's output is
the same as ParseTree's output: s-expressions using ruby's arrays and
base types.
As an example:
def conditional1(arg1)
if arg1 == 0 then
return 1
end
return 0
end
becomes:
s(:defn, :conditional1,
s(:args, :arg1),
s(:scope,
s(:block,
s(:if,
s(:call, s(:lvar, :arg1), :==, s(:arglist, s(:lit, 0))),
s(:return, s(:lit, 1)),
nil),
s(:return, s(:lit, 0)))))


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod 755
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib -type f | xargs chmod 644
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test -type f | xargs chmod 755
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby/, "/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/*

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/ruby_parse
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.5-1mdv2011.0
+ Revision: 585876
- import rubygem-ruby_parser

