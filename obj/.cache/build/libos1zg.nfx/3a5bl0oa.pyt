<!DOCTYPE html>
<!--[if IE]><![endif]-->
<html>
  
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Data Output Formats </title>
    <meta name="viewport" content="width=device-width">
    <meta name="title" content="Data Output Formats ">
    <meta name="generator" content="docfx 2.42.1.0">
    
    <link rel="shortcut icon" href="../../favicon.ico">
    <link rel="stylesheet" href="../../styles/docfx.vendor.css">
    <link rel="stylesheet" href="../../styles/docfx.css">
    <link rel="stylesheet" href="../../styles/main.css">
    <meta property="docfx:navrel" content="../../toc.html">
    <meta property="docfx:tocrel" content="../toc.html">
    
    <meta property="docfx:rel" content="../../">
    
  </head>
  <body data-spy="scroll" data-target="#affix" data-offset="120">
    <div id="wrapper">
      <header>
        
        <nav id="autocollapse" class="navbar navbar-inverse ng-scope" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="../../index.html" width="46">
                <img id="logo" src="../../Documentation/images/atlas_icon.png" height="46" width="46" alt="OSIsoft Cloud Serices"> 
              </a>
            </div>
            <div class="collapse navbar-collapse" id="navbar">
              <form class="navbar-form navbar-right" role="search" id="search">
                <div class="form-group">
                  <input type="text" class="form-control" id="search-query" placeholder="Search" autocomplete="off">
                </div>
              </form>
            </div>
          </div>
        </nav>
        
        <div class="subnav navbar navbar-default">
          <div class="container hide-when-search" id="breadcrumb">
            <ul class="breadcrumb">
              <li></li>
            </ul>
          </div>
        </div>
      </header>
      <div class="container body-content">
        
        <div id="search-results">
          <div class="search-list"></div>
          <div class="sr-items">
            <p><i class="glyphicon glyphicon-refresh index-loading"></i></p>
          </div>
          <ul id="pagination"></ul>
        </div>
      </div>
      <div role="main" class="container body-content hide-when-search">
        
        <div class="sidenav hide-when-search">
          <a class="btn toc-toggle collapse" data-toggle="collapse" href="#sidetoggle" aria-expanded="false" aria-controls="sidetoggle">Show / Hide Table of Contents</a>
          <div class="sidetoggle collapse" id="sidetoggle">
            <div id="sidetoc"></div>
          </div>
        </div>
        <div class="article row grid-right">
          <div class="col-md-10">
            <article class="content wrap" id="_content" data-uid="DataOutputFormats">
<h1 id="data-output-formats" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="5" sourceendlinenumber="5">Data Output Formats</h1>

<p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="7" sourceendlinenumber="7">Data View Data can be viewed in the following formats: <a href="#default" data-raw-source="[default](#default)" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="7" sourceendlinenumber="7">default</a>, <a href="#table" data-raw-source="[table](#table)" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="7" sourceendlinenumber="7">table</a> and <a href="#csv" data-raw-source="[csv](#csv)" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="7" sourceendlinenumber="7">csv</a>. Table and csv also have the option of including headers. Provide the output format using the form parameter in Data call parameter list.</p>
<h2 id="a-namedefaultdefault-format-a" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="9" sourceendlinenumber="9"><a name="default"><code>Default Format</code> </a></h2>
<p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="11" sourceendlinenumber="11">The following is a request to retrieve Data using the default output</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="12" sourceendlinenumber="14"><code class="lang-text">     GET api/v1/Tenants/{tenantId}/Namespaces/{namespaceId}/DataView/Simple/Data/Interpolated
</code></pre><pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="15" sourceendlinenumber="36"><code>  Content-Type: application/json

[
    {
        &quot;Time&quot;: &quot;2018-01-01T00:00:00Z&quot;,
        &quot;Temperature&quot;: 24,
        &quot;Flowrate&quot;: 44,
        &quot;Volume&quot;: 245
    },
    {
        &quot;Time&quot;: &quot;2018-01-01T00:00:01Z&quot;,
        &quot;Temperature&quot;: 24,
        &quot;Flowrate&quot;: 44,
        &quot;Volume&quot;: 245
    },
    {
        &quot;Time&quot;: &quot;2018-01-01T00:00:02Z&quot;,
        &quot;Temperature&quot;: 24,
        &quot;Flowrate&quot;: 44,
        &quot;Volume&quot;: 245
    }
]
</code></pre><h2 id="a-nametabletable-output-format-a" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="38" sourceendlinenumber="38"><a name="table"><code>Table Output Format</code> </a></h2>
<p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="41" sourceendlinenumber="41">The following is a request to retrieve Data in a Table format without headers</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="42" sourceendlinenumber="45"><code class="lang-text">     GET api/v1/Tenants/{tenantId}/Namespaces/{namespaceId}/DataView/Simple/Data/Interpolated
     /form=table
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="46" sourceendlinenumber="46">The following response would be returned from the above code:</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="48" sourceendlinenumber="88"><code>  Content-Type: application/json

  {
     &quot;Columns&quot;: [
        {
            &quot;Name&quot;: &quot;Time&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Temperature&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Flowrate&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Volume&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        }
    ],
    &quot;Rows&quot;: [
    [
        &quot;2018-01-01T00:00:00Z&quot;,
        24,
        44,
        245
    ],
    [
        &quot;2018-01-01T00:00:01Z&quot;,
        24,
        44,
        245
    ],
    [
        &quot;2018-01-01T00:00:02Z&quot;,
        24,
        44,
        245
    ]
  }
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="90" sourceendlinenumber="90">The following is a request to retrieve Data in a Table format with headers</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="91" sourceendlinenumber="94"><code class="lang-text">     GET api/v1/Tenants/{tenantId}/Namespaces/{namespaceId}/DataView/Simple/Data?Interpolated
     /form=tableh
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="95" sourceendlinenumber="95">The following response would be returned from the above code:</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="97" sourceendlinenumber="143"><code>  Content-Type: application/json

  {
    &quot;Columns&quot;: [
        {
            &quot;Name&quot;: &quot;Time&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Temperature&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Flowrate&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        },
        {
            &quot;Name&quot;: &quot;Volume&quot;,
            &quot;Type&quot;: &quot;Object&quot;
        }
    ],
    &quot;Rows&quot;: [
        [
            &quot;Time&quot;,
            &quot;Temperature&quot;,
            &quot;Flowrate&quot;,
            &quot;Volume&quot;
        ],
        [
            &quot;2018-01-01T00:00:00Z&quot;,
            24,
            44,
            245
        ],
        [
            &quot;2018-01-01T00:00:01Z&quot;,
            24,
            44,
            245
        ],
        [
            &quot;2018-01-01T00:00:02Z&quot;,
            24,
            44,
            245
        ]
]
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="144" sourceendlinenumber="144">}</p>
<h2 id="a-namecsvcsv-output-format-a" sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="146" sourceendlinenumber="146"><a name="csv"><code>CSV Output Format</code> </a></h2>
<p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="148" sourceendlinenumber="148">The following is a request to retrieve Data in a csv format without headers</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="149" sourceendlinenumber="152"><code class="lang-text">     GET api/v1/Tenants/{tenantId}/Namespaces/{namespaceId}/DataView/Simple/Data?Interpolated
     ?form=csv
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="153" sourceendlinenumber="153">The following response would be returned from the above code:</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="155" sourceendlinenumber="159"><code>  Content-Type: text/csv

  2018-01-01T00:00:00Z,24,44,245
  2018-01-01T00:00:01Z,24,44,245
  2018-01-01T00:00:02Z,24,44,245
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="161" sourceendlinenumber="161">The following is a request to retrieve Data in a csv format with headers (csvh)</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="162" sourceendlinenumber="165"><code class="lang-text">     GET api/v1/Tenants/{tenantId}/Namespaces/{namespaceId}/DataView/Simple/Data?Interpolated
     ?form=csvh
</code></pre><p sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="166" sourceendlinenumber="166">The following response would be returned from the above code:</p>
<pre sourcefile="Documentation/DataViews/DataOutputFormats.md" sourcestartlinenumber="168" sourceendlinenumber="173"><code>  Content-Type: text/csv

  Time,Temperature,Flowrate,Volume
  2018-01-01T00:00:00Z,24,44,245
  2018-01-01T00:00:01Z,24,44,245
  2018-01-01T00:00:02Z,24,44,245
</code></pre></article>
          </div>
          
          <div class="hidden-sm col-md-2" role="complementary">
            <div class="sideaffix">
              <div class="contribution">
                <ul class="nav">
                  <li>
                    <a href="https://github.com/osisoft/OCS-Docs/blob/master/Documentation/DataViews/DataOutputFormats.md/#L1" class="contribution-link">Improve this Doc</a>
                  </li>
                </ul>
              </div>
              <nav class="bs-docs-sidebar hidden-print hidden-xs hidden-sm affix" id="affix">
              <!-- <p><a class="back-to-top" href="#top">Back to top</a><p> -->
              </nav>
            </div>
          </div>
        </div>
      </div>
      
      <footer>
        <div class="grad-bottom"></div>
        <div class="footer">
            <span id='copyright-text'>© 2019 - OSIsoft, LLC.<span>
        </span></span></div>
      </footer>
    </div>
    
    <script type="text/javascript" src="../../styles/docfx.vendor.js"></script>
    <script type="text/javascript" src="../../styles/docfx.js"></script>
    <script type="text/javascript" src="../../styles/main.js"></script>
  </body>
</html>
